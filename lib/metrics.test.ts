import {test} from 'node:test';import assert from 'node:assert/strict';import {metrics,change,current,csv} from './metrics.ts';
const m=metrics.find(m=>m.id==='inflation')!;
test('rates use percentage points and matching months',()=>{const r=[{period:'2024-01','12-month inflation':8},{period:'2025-01','12-month inflation':5},{period:'2025-02','12-month inflation':6}];assert.deepEqual(change(r,m,2024),null);assert.deepEqual(change(r.slice(0,2),m,2025),{value:-3,unit:'pp'});assert.equal(change(r,m,2025),null)});
test('year cutoff excludes later observations and missing values',()=>{assert.equal(current([{period:'2024-01','12-month inflation':2},{period:'2025-01','12-month inflation':null},{period:'2026-01','12-month inflation':4}],m,2025)?.period,'2024-01')});
test('negative trade balance compares absolute change, not misleading growth',()=>{const b=metrics.find(m=>m.id==='balance')!;assert.deepEqual(change([{period:'2024-01','Trade balance':-100000},{period:'2025-01','Trade balance':-120000}],b,2025),{value:-20,unit:'KES bn'})});
test('CSV escapes quotes and delimiters',()=>assert.equal(csv([['a,b','say "hello"']]),'"a,b","say ""hello"""'));
