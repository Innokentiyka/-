run:
	docker compose --env-file track_habits/.env up --build -d
dev:
	docker compose --env-file track_habits/.env up --build
stop:
	docker compose stop