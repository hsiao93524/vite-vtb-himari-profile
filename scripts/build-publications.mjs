import { execFileSync } from 'node:child_process'
import { rmSync } from 'node:fs'
import { join } from 'node:path'

const nodeBin = process.execPath
const tscBin = join('node_modules', 'typescript', 'bin', 'tsc')
const viteBin = join('node_modules', 'vite', 'bin', 'vite.js')

function run(command, args) {
  execFileSync(command, args, {
    stdio: 'inherit',
    windowsHide: true,
  })
}

rmSync('dist', { force: true, recursive: true })

run(nodeBin, [tscBin, '-b'])
run(nodeBin, [viteBin, 'build', '--mode', 'public', '--outDir', 'dist'])
run(nodeBin, [
  viteBin,
  'build',
  '--mode',
  'hr',
  '--outDir',
  'dist/hr',
  '--emptyOutDir',
  'false',
])
