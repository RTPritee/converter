from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import json
import io

app = FastAPI()  #creating instance 

@app.post("/convert")
async def convert(file: UploadFile):
    try:
        # file read , the uploaded json file
        content = await file.read()
        
        # JSON content parse
        data = json.loads(content)

        # Extracting keys and prepare rows
        keys = data.keys()
        rows = []
        max_row_count = max(len(data[key]) for key in keys)

        for i in range(max_row_count):
            row = {}
            for key in keys:
                try:
                    value = data[key][i]["value"]
                except (IndexError, KeyError):
                    value = "*"  # for invalid or missing value it will provide * (asterisks)
                row[key] = value
            rows.append(row)

        # Converting the rows into a DataFrame
        df = pd.DataFrame(rows)

        # date formatting 
        if "gregorian_date" in df.columns:
            df["gregorian_date"] = pd.to_datetime(df["gregorian_date"], errors="coerce").dt.strftime("%m/%d/%Y").fillna("*")

        # Creating a CSV stream for downloading
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)

        
        # Return CSV file as response
        return StreamingResponse(
            output,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=output.csv"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during conversion: {str(e)}")

@app.get("/")
async def root():
    return {"message": "FastAPI JSON to CSV Converter is running!"}
