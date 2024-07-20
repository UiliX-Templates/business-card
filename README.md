## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**Production:**

```bash
pip install -r requirements/production.txt
```

**Development:**

```bash
pip install -r requirements/development.txt
```

```bash
npm install
```

## Changes

`pyproject.toml`

```text
docker-l1 = "*:docker build -f Dockerfile-L1 -t |>> project_name_l1 <<| ."
```

`Dockerfile-L2`

```text
FROM |>> project_name_l1 <<| (this has to match above)
```

`docker-compose.yml`

```text
container_name: |>> project_name <<|
```

`app/business_info.py`

```text
Change business info to match your business...
```

### Replace Favicons

**NOTE:** Only changeable in a development environment.

```bash
pyhead favicons -s [file].[png, jpg, jpeg, gif, svg, tiff] -d app/static/favicons -scg
```

## Deployment

```bash
git clone [repository] && cd [repository]
```

```bash
pyqwe docker-l1
```

```bash
pyqwe docker-deploy
```

**Update deployment:**

```bash
cd [repository]
```

```bash
git pull && pyqwe docker-deploy
```