import pathlib
import sys
import tomllib
import jinja2


def main():
    #tomlを読み込む
    toml_path = pathlib.Path("config.toml")
    config = tomllib.load(open(toml_path, "rb"))

    # rootDirの一階層したのディレクトリ内のindex.htmlのpathとそのディレクトリ名を取得
    index_files = []
    for path in pathlib.Path(config["config"]["rootDir"]).iterdir():
        if path.is_dir():
            index_file = path / "index.html"
            if index_file.exists():
                index_files.append((index_file, path.name))

    # index.htmlをtemplateをもとに作成
    template_path = pathlib.Path("template/index.html")
    template = jinja2.Template(open(pathlib.Path("template.html"), "r").read())



    index_html = template.render(items=index_files)


    output_path = pathlib.Path(config["config"]["rootDir"]) / "index.html"
    with open(output_path, "w") as output_file:
        output_file.write(index_html)

    print(f"Index file created at: {output_path}")


if __name__ == "__main__":
    main()
