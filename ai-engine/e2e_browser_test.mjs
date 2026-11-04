// -*- coding: utf-8 -*-
import { spawn } from 'child_process';
import http from 'http';
import os from 'os';
import path from 'path';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9222;
const HTML_PATH = "file:///C:/Users/inche/Antigravity/tokyo-trip-assistant/index.html";
const TEMP_PROFILE = path.join(os.tmpdir(), "chrome_test_profile_" + Date.now());

console.log("=" .repeat(60));
console.log("🌐 STARTING HEADLESS CHROME E2E RUNTIME SIMULATION");
console.log("=" .repeat(60));

// 1. Launch Chrome Headless with clean isolated profile
const chromeProc = spawn(CHROME_PATH, [
  '--headless=new',
  `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${TEMP_PROFILE}`,
  '--disable-gpu',
  '--no-first-run',
  '--no-default-browser-check',
  '--allow-file-access-from-files',
  HTML_PATH
], { stdio: 'ignore' });

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getWsUrl() {
  for (let i = 0; i < 20; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/list`);
      const data = await res.json();
      const page = data.find(item => item.type === 'page' && !item.url.startsWith('chrome-extension://'));
      if (page && page.webSocketDebuggerUrl) {
        return page.webSocketDebuggerUrl;
      }
    } catch (e) {}
    await sleep(300);
  }
  throw new Error("Unable to connect to Chrome CDP within timeout");
}

async function runTest() {
  const wsUrl = await getWsUrl();
  console.log(`Connected to Chrome DevTools Protocol at: ${wsUrl}`);

  const ws = new WebSocket(wsUrl);
  let id = 1;
  const pending = new Map();
  const consoleErrors = [];
  const runtimeExceptions = [];

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.method === "Runtime.exceptionThrown") {
      runtimeExceptions.push(msg.params.exceptionDetails);
    }
    if (msg.method === "Console.messageAdded" && msg.params.message.level === "error") {
      consoleErrors.push(msg.params.message.text);
    }
    if (msg.id && pending.has(msg.id)) {
      const cb = pending.get(msg.id);
      pending.delete(msg.id);
      cb(msg);
    }
  };

  await new Promise(res => ws.onopen = res);

  function sendCommand(method, params = {}) {
    return new Promise((resolve, reject) => {
      const curId = id++;
      pending.set(curId, (resp) => {
        if (resp.error) reject(resp.error);
        else resolve(resp.result);
      });
      ws.send(JSON.stringify({ id: curId, method, params }));
    });
  }

  await sendCommand("Runtime.enable");
  await sendCommand("Console.enable");
  await sendCommand("Page.enable");

  console.log("\n⏳ Navigating to index.html...");
  const navResult = await sendCommand("Page.navigate", { url: HTML_PATH });
  console.log("Page.navigate result:", navResult);
  await sleep(2000);
  console.log("Current URL:", await evaluate("window.location.href"));

  async function evaluate(expr) {
    const res = await sendCommand("Runtime.evaluate", {
      expression: expr,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      console.error("DEBUG EXCEPTION:", JSON.stringify(res.exceptionDetails, null, 2));
      runtimeExceptions.push(res.exceptionDetails);
      throw new Error(`Evaluation failed: ${res.exceptionDetails.text}`);
    }
    return res.result ? res.result.value : undefined;
  }

  console.log("👉 Test 1: Verifying active initial view and DOM titles...");
  const title = await evaluate("document.title");
  console.log(`  • Document Title: "${title}"`);

  console.log("👉 Test 2: Testing all 5 navigation tabs switching...");
  for (const tab of ["funliday", "gemini", "pokemon", "deadlines", "tickets", "funliday"]) {
    await evaluate(`switchNavTab('${tab}')`);
    await sleep(200);
    const isVisible = await evaluate(`document.getElementById('view${tab.charAt(0).toUpperCase() + tab.slice(1)}').style.display !== 'none'`);
    if (!isVisible) throw new Error(`Tab ${tab} failed to become visible!`);
    console.log(`  • Tab "${tab}" switch verified visible`);
  }

  console.log("👉 Test 3: Testing all 5 AI mode selector states...");
  for (const mode of ["detailed", "serious", "relaxed", "brief", "concise"]) {
    await evaluate(`selectMode('${mode}')`);
    await sleep(100);
    const activeMode = await evaluate("currentMode");
    if (activeMode !== mode) throw new Error(`Mode switch to ${mode} failed!`);
    console.log(`  • AI Mode "${mode}" active`);
  }

  console.log("👉 Test 4: Testing Pokemon checklist toggle & state persistence...");
  await evaluate("switchNavTab('pokemon')");
  await sleep(400);
  const initialDone = await evaluate("!!checkedPokes['pk1']");
  await evaluate("togglePoke('pk1')");
  const toggledDone = await evaluate("!!checkedPokes['pk1']");
  if (initialDone === toggledDone) throw new Error("Pokemon togglePoke failed to toggle state!");
  console.log(`  • Pokemon 'pk1' state successfully toggled (${initialDone} -> ${toggledDone})`);
  // Revert back
  await evaluate("togglePoke('pk1')");

  console.log("👉 Test 5: Testing Leaflet Map actions & Pan...");
  await evaluate("fitAllPokemonSpots()");
  await sleep(300);
  await evaluate("panToPoke('pk1')");
  await sleep(300);
  console.log("  • Leaflet fitAllPokemonSpots & panToPoke passed");

  console.log("👉 Test 6: Testing Deadlines View toggle expired items...");
  await evaluate("switchNavTab('deadlines')");
  await sleep(200);
  await evaluate("toggleExpiredDeadlines()");
  await sleep(200);
  await evaluate("toggleExpiredDeadlines()");
  console.log("  • Deadlines toggleExpiredDeadlines passed");

  console.log("👉 Test 7: Testing Topic creation & deletion...");
  await evaluate(`
    const newT = { id: 'test_' + Date.now(), name: 'Test Topic', history: [] };
    topics.push(newT);
    currentTopicId = newT.id;
    saveTopics();
    renderTopicSelector();
    renderChatHistory();
  `);
  const topicLen = await evaluate("topics.length");
  console.log(`  • Created test topic, total topics: ${topicLen}`);
  await evaluate(`
    topics = topics.filter(t => !t.id.startsWith('test_'));
    currentTopicId = topics[0].id;
    saveTopics();
    renderTopicSelector();
    renderChatHistory();
  `);
  console.log("  • Cleaned up test topic");

  console.log("👉 Test 8: Verifying zero runtime exceptions or console errors...");
  console.log(`  • Uncaught Runtime Exceptions: ${runtimeExceptions.length}`);
  console.log(`  • Console Errors: ${consoleErrors.length}`);

  if (runtimeExceptions.length > 0) {
    console.error("❌ Fatal Runtime Exceptions detected:", runtimeExceptions);
  }
  if (consoleErrors.length > 0) {
    console.warn("⚠️ Console Errors detected:", consoleErrors);
  }

  const allPassed = runtimeExceptions.length === 0 && consoleErrors.length === 0;

  ws.close();
  chromeProc.kill();
  try {
    fs.rmSync(TEMP_PROFILE, { recursive: true, force: true });
  } catch (e) {}

  if (allPassed) {
    console.log("\n" + "=" .repeat(60));
    console.log("🎉 ALL E2E BROWSER TESTS PASSED WITH 0 ERRORS & 0 EXCEPTIONS!");
    console.log("=" .repeat(60));
    process.exit(0);
  } else {
    console.error("\n❌ E2E TESTS FAILED!");
    process.exit(1);
  }
}

runTest().catch(err => {
  console.error("Test execution fatal error:", err);
  chromeProc.kill();
  process.exit(1);
});
