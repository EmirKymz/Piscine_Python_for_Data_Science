import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        if not path.endswith(".csv"):
            raise ValueError("File must be a CSV file")
        res = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({res.shape[0]}, {res.shape[1]})")
        return res
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError as e:
        print(e)
        return None
    except Exception as e:
        print("An error occurred: ", e)
        return None

