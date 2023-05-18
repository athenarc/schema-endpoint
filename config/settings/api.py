from config.env import env

TASK_API = {
    'TASK_API_CLASS': env.str('SCHEMA_API_TASK_API_CLASS'),
    'GET_TASK_ENDPOINT': env.str('SCHEMA_API_TASK_API_GET_ENDPOINT'),
    'CREATE_TASK_ENDPOINT': env.str('SCHEMA_API_TASK_API_CREATE_ENDPOINT'),
    'DB_TASK_STATUS_TTL_SECONDS': env.int('SCHEMA_API_TASK_API_STATUS_TTL_SECONDS', 5)
}

CONTEXT_MINIMUM_RESOURCES = {
    'CPU': env.int('SCHEMA_API_CONTEXT_MIN_CPU', 1),
    'RAM_GB': env.int('SCHEMA_API_CONTEXT_MIN_RAM_GB', 1),
    'TASKS': env.int('SCHEMA_API_CONTEXT_MIN_TASKS', 1),
    'ACTIVE_TASKS': env.int('SCHEMA_API_CONTEXT_MIN_ACTIVE_TASKS', 1),
    'PROCESS_TIME_SECONDS': env.int('SCHEMA_API_CONTEXT_MIN_PROCESS_TIME_SECONDS', 10 * 60)
}
