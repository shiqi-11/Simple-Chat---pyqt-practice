from upstash_ratelimit import Ratelimit, TokenBucket
from upstash_redis import Redis


def checkLimit():
    ratelimit = Ratelimit(
        redis=Redis.from_env(),
        limiter=TokenBucket(max_tokens=3, refill_rate=3, interval=30),
        # refill the bucket with 3 tokens every 30 seconds
    )
    response = ratelimit.block_until_ready("IP", timeout=30)
    return response.allowed
