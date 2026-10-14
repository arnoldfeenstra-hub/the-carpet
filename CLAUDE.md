# The Carpet

A rotation screener for Hyperliquid perps, reverse-engineered from two screenshots
(`docs/reverse-engineering.md`). It places each coin of a group on the relative-rotation
plane, draws the group as a quadrant treemap sized by money traded, and reads five things
per tile: the session, the web, the strings, the liquidity and the rotation. Clicking a tile
opens a chart with boxes, TPR turns, an up-rung EMA, VWAP and a volume heat strip.

It describes the tape. It does not forecast it.

## Hard rules

1. **No trade execution, ever.** No exchange keys, no signing, no order placement, no
   order ticket on the page. The Hyperliquid reader (`rotation/hyperliquid.py`) can reach
   only the read-only `/info` URL and send only the two allowlisted queries in
   `ALLOWED_QUERY_TYPES`; `tests/test_rotation.py` inspects the module to hold that.
2. **Never describe a reading as predictive.** No reading has been tested for what comes
   next. Do not add backtest claims (the screenshot's "the fade the study paid" was left
   out on purpose). A claim of edge needs an out-of-sample, forward-in-time test with the
   base rate and confidence intervals reported next to it, and that study does not exist.
3. **Never impute.** A bar a coin did not print is missing, not filled. A reading whose
   window is short of bars is `None` with a reason. A coin with no reported size is listed
   beneath the carpet, never drawn at a guessed size. `NaN` from the API is missing data.
4. **No secrets in the repo.** Nothing here needs a key; keep it that way.
5. **Synthetic data is always labelled.** `web/carpet-demo.json` comes from
   `rotation/synthetic.py`, carries `"synthetic": true`, and the page shows it under a red
   SYNTHETIC banner. Never present it, or anything derived from it, as market data.

## Conventions

- Python 3.11+, stdlib only at runtime: `api/carpet.py` runs as a Vercel function with
  nothing installed. `uv` for dev deps, `ruff` for lint, `pytest` for tests.
- Tests never open a socket (`tests/conftest.py` enforces it). Use `SyntheticInfo` or a
  stub opener.
- After changing anything that feeds the demo, regenerate it with
  `python -m rotation.synthetic`; a test fails when `web/carpet-demo.json` is stale.
- All timestamps UTC, epoch millis. The page shows ET.
- When a reverse-engineered rule changes, update `docs/reverse-engineering.md` in the same
  commit: it is the record of what was inferred and how sure the inference is.
