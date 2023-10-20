
from sample import create_app, sample_app
import dotenv
# If you want to use environment variables:

dotenv.load_dotenv(".env")

app = create_app()
sample_app.setup(app)

app.run("localhost", 8000)