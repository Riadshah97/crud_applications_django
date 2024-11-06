import time
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set rate limit values from settings, or default values
        self.limit = getattr(settings, 'RATE_LIMIT_REQUESTS', 100)  # Max requests per IP
        self.window = getattr(settings, 'RATE_LIMIT_WINDOW', 60)  # Time window in seconds

    def __call__(self, request):
        # Get IP address
        ip_address = self.get_client_ip(request)
        
        # Create a cache key specific to the IP
        cache_key = f'rate_limit:{ip_address}'
        
        # Get or set default data from cache: request count and timestamp
        data = cache.get(cache_key, [0, time.time()])
        request_count, start_time = data

        # Reset counter if the time window has passed
        if time.time() - start_time > self.window:
            request_count = 0
            start_time = time.time()

        # Increment request count
        request_count += 1

        # Store updated data in cache
        cache.set(cache_key, [request_count, start_time], timeout=self.window)

        # Check if request count exceeds the limit
        if request_count > self.limit:
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

        # Process the request if under the limit
        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        # Get the client IP address, checking for reverse proxy headers
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
