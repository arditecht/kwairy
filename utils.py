import typing



def run_query():
    pass

def check_query():
    pass

# a helper decorator for any llm api calls for rate limiting in place for openai servers
def rate_limit(fun: typing.Callable) -> typing.Callable :
    from tenacity import (retry, stop_after_attempt, wait_random_exponential) # for exponential backoff
    @retry (wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def _with_backoff_ (**kwargs) :
        return fun(**kwargs)
    return _with_backoff_
