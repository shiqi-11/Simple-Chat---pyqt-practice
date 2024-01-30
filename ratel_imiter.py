import redis
from redis_rate_limit import RateLimit, TooManyRequests

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)


def checkLimit(user_ip):
    try:
        with RateLimit(resource='users_list', client=user_ip, max_requests=5, expire=20, redis_pool=redis_pool):
            return True
    except TooManyRequests:
        return False