# Theatre-project

API service for a theatre allowing online reservations and seat selections.

## Installation

### Using GitHub

```bash
git clone https://github.com/VitalyBashkiser/Theatre-project.git
cd Theatre-project
python -m venv .venv
source .\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
