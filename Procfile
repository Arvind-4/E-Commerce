release: bash commands/release-tasks.sh
web: sh -c 'cd web && gunicorn backend.asgi.production:application --workers 4 --worker-class uvicorn.workers.UvicornWorker'