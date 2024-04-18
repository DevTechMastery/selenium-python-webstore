import os


# Function to get the base URL based on the environment
def get_base_url():
    # Get the environment variable 'ENV'. If it's not set, default to 'prod'
    env = os.environ.get('ENV', 'prod')

    # If the environment is 'test', return the test URL
    if env.lower() == 'test':
        return 'http://happyharbor.sandbox.local'
    # If the environment is 'prod', return the production URL
    elif env.lower() == 'prod':
        return 'http://happyharbor.local'
    # If the environment is neither 'test' nor 'prod', raise an exception
    else:
        raise Exception(f"Unknown environment: {env}")
