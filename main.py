import os
from langflow import run

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    run(host="0.0.0.0", port=port)

