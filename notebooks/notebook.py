import marimo as mo

__generated_with = "0.19.4"
app = mo.App()


@app.cell
def _():
    return mo.md("Benchlet notebook is running ✅")


if __name__ == "__main__":
    app.run()
