import { spawn } from 'child_process';
import path from 'path';
import os from 'os';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9226;
const TEMP_PROFILE = path.join(os.tmpdir(), "chrome_cap_" + Date.now());
const ARTIFACT_DIR = "C:\\Users\\inche\\.gemini\\antigravity\\brain\\91597ac8-c416-4cbe-bae7-680f6b777a9a";

const proc = spawn(CHROME_PATH, [
  '--headless=new',
  `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${TEMP_PROFILE}`,
  '--allow-file-access-from-files',
  'file:///C:/Users/inche/Antigravity/tokyo-trip-assistant/index.html'
]);

await new Promise(r => setTimeout(r, 1500));
const res = await fetch(`http://127.0.0.1:${PORT}/json/list`);
const list = await res.json();
const page = list.find(item => item.type === 'page' && !item.url.startsWith('chrome-extension://'));
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);

let id = 1;
function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const cur = id++;
    const handler = (e) => {
      const msg = JSON.parse(e.data);
      if (msg.id === cur) {
        ws.removeEventListener('message', handler);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id: cur, method, params }));
  });
}

await send('Page.enable');
await send('Runtime.enable');

// Emulate iPhone 14/15 (390 x 844, scale factor 2)
await send('Emulation.setDeviceMetricsOverride', {
  width: 390,
  height: 844,
  deviceScaleFactor: 2,
  mobile: true
});

async function captureTab(tabName, filename, jsCode = '') {
  await send('Runtime.evaluate', { expression: `switchNavTab('${tabName}')` });
  if (jsCode) {
    await send('Runtime.evaluate', { expression: jsCode });
  }
  await new Promise(r => setTimeout(r, 800));

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  const outPath = path.join(ARTIFACT_DIR, filename);
  fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
  console.log(`📸 Saved ${filename} (${fs.statSync(outPath).size} bytes)`);
}

console.log("Capturing 390x844 pixel-perfect mobile screenshots...");
await captureTab('funliday', 'screen_v152_01_funliday.png');
await captureTab('gemini', 'screen_v152_02_gemini_clean.png');
await captureTab('pokemon', 'screen_v152_03_pokemon_map.png');
await captureTab('deadlines', 'screen_v152_04_deadlines.png');
await captureTab('tickets', 'screen_v152_05_tickets.png');
await captureTab('gemini', 'screen_v152_06_settings_modal.png', 'openSettingsModal()');

// Test 375px narrow width (iPhone SE / 8)
await send('Emulation.setDeviceMetricsOverride', {
  width: 375,
  height: 667,
  deviceScaleFactor: 2,
  mobile: true
});
await captureTab('funliday', 'screen_v152_07_mobile_375px.png', 'closeSettingsModal()');

ws.close();
proc.kill();
try { fs.rmSync(TEMP_PROFILE, { recursive: true, force: true }); } catch (e) {}
console.log("🎉 All mobile screenshots captured successfully!");
