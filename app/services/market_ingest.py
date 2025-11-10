# small stub to show how ingestion could be wired
import asyncio


async def fetch_provider_snapshot(provider, symbols):
await asyncio.sleep(0.1)
return [{'symbol': s, 'ts': '2025-11-09T00:00:00Z', 'price': 100.0} for s in symbols]
