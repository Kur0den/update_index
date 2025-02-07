import pathlib
import sys
import tomllib


def main():
    #tomlを読み込む
    toml_path = pathlib.Path("config.toml")
    config = tomllib.load(toml_path)

    # rootDirの一階層したのディレクトリ内のindex.htmlのpathとそのディレクトリ名を取得
    index_files = []
    for path in pathlib.Path(config["rootDir"]).iterdir():
        if path.is_dir():
            index_file = path / "index.html"
            if index_file.exists():
                index_files.append((index_file, path.name))

    print(index_files)

if __name__ == "__main__":
    main()
