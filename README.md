# A simple business card website.

![screenshot.png](_assets%2Fscreenshot.png)

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
```

### Production:

```bash
pip install -r requirements/production.txt
```

#### Run

```bash
gunicorn
```

### Development:

```bash
pip install -r requirements/development.txt
```

```bash
npm install
```

#### Run

`terminal 1`

```bash
pyqwe debug
```

`terminal 2`

```bash
pyqwe tailwind-watch
```

### Docker:

#### !!! Change Files !!!

`Dockerfile-L2`

```text
FROM <LAYER 1 IMAGE NAME>

Example: FROM my_project_l1
```

`docker-compose.yml`

```text
container_name: <CONTAINER NAME>

Example: my_project (will show as business_card_my_project in docker)
```

#### Build and Run

```bash
docker build -f Dockerfile-L1 -t <LAYER 1 IMAGE NAME> .

# Example: docker build -f Dockerfile-L1 -t my_project_l1 .
```

```bash
docker-compose up -d --build
```

## Files to Update

```text
app/business_info.py
```

## Replace Favicons

**NOTE:** Only changeable in a development environment.

```bash
pyhead favicons -s [file].[png, jpg, jpeg, gif, svg, tiff] -d app/static/favicons -scg
```

### Update from _assers/raw_favicon.png

Overwrite the `_assers/raw_favicon.png` file with the new favicon.

```bash
pyqwe update-favicons
```

## Update in Deployment

```bash
git pull && docker-compose up -d --build
```