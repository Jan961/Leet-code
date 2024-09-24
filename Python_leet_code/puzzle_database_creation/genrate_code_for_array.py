from pathlib import Path

dir_path = Path(__file__).parent.absolute()


with open(dir_path.joinpath("generated.txt"), "w") as f:
    for i in range(2,201):
        number = str(i).rjust(3,'0')
        f.write(f"{i} to R.drawable.p{number},\n")
    for i in range(317,384):
        number = str(i).rjust(3,'0')
        f.write(f"{i} to R.drawable.p{number},\n")


