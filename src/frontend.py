from frontend import ExcelValidadorUI
from backend import process_excel

def display_results(self, result, error):
    if error:
        st.error(f"Erro na validação: {error}")
    else:
        st.success("O schema do arquivo Excel está correto!")

def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        result, error = process_excel(upload_file)
        ui.display_results(result, error)

if __name__ == "__main__":
    main()