from dotenv import load_dotenv
import os
load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
TEST_DB_NAME = os.environ.get("TES_DB_NAME")