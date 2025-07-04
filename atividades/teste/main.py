


novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo salvo com sucesso.")
            continue