# The Carpet

A rotation screener for Hyperliquid perps, rebuilt from two screenshots.

It shows a treemap of a group of coins, split into the four relative-rotation quadrants
(Leading, Weakening, Lagging, Improving) and sized by money traded. Each tile reads five
things:

- **the session**: change since the UTC day open;
- **the web**: rich or cheap to the group after beta;
- **the strings**: pair-spread stretch against each correlated coin, and which pair is
  tautest;
- **the liquidity**: recent money traded against the coin's own norm, hot or thin;
- **the rotation**: the quadrant.

THE CROSS shows how much of the money sits on the strong side of the plane, and chips the
coins that are mid-turn with a rich or cheap web behind them. Clicking a tile opens a chart
with EMA 9, session VWAP, an up-rung EMA, BOX zones, TPR turns and a volume heat strip.

**Every reading is descriptive.** None has been tested for what comes next, and there is
no code path to an order. How each reading was reverse-engineered, and how sure each
inference is, is in [docs/reverse-engineering.md](docs/reverse-engineering.md).

## Run it

Data comes from Hyperliquid's public read-only `/info` endpoint. It needs no key.

```bash
python -m rotation.carpet --group hl-crypto --read-on 1h   # the readings, as a table
python -m rotation.synthetic                               # regenerate the demo data
```

On Vercel, `web/index.html` is the page and `api/carpet.py` serves it live:

- `/api/carpet?group=hl-crypto&read_on=1h` returns the carpet.
- `/api/carpet?chart=BTC&interval=5m&bars=800` returns one coin's chart.

Without the endpoint, the page falls back to `web/carpet-demo.json`. That is a synthetic
market, and the page shows it under a red SYNTHETIC banner.

## Develop

```bash
uv venv && uv pip install -e ".[dev]"
ruff check . && pytest -q          # offline; tests/conftest.py blocks the network
```
