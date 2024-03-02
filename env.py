import os  # Import os module

# Set the DATABASE_URL environment variable for PostgreSQL database connection
os.environ["DATABASE_URL"] = (
    "postgres://paupmyzc:WsFo7M53s4CaLiUq9fek7AHXnrm4Pn5n@"
    "abul.db.elephantsql.com/paupmyzc"
)
# Set the SECRET_KEY environment variable for Django application security
os.environ["SECRET_KEY"] = "SomeThingInTheWay!1666"
# Set the CLOUDINARY_URL environment variable for Cloudinary configuration
os.environ["CLOUDINARY_URL"] = (
    "cloudinary://433257183135994:nR7taDJZ-0nrbeji9ETYTxX25QE@"
    "dtyqoklv7"
)
os.environ["DEBUG"] = "False"
# os.environ["DEPLOYMENT"] = "True"
os.environ["CLOUDINARY_CLOUD_NAME"] = "dtyqoklv7"
os.environ["CLOUDINARY_API_KEY"] = "433257183135994"
os.environ["CLOUDINARY_API_SECRET"] = "nR7taDJZ-0nrbeji9ETYTxX25QE"
