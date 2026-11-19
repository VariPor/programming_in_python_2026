from PIL import Image


def grayscale_functional(input_path: str, output_path: str) -> None:
    img = Image.open(input_path).convert("RGB")

    gray_data = list(
        map(
            lambda p: (lambda v: (v, v, v))(
                int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
            ),
            img.getdata(),
        )
    )

    out = Image.new("RGB", img.size)
    out.putdata(gray_data)
    out.save(output_path)


if __name__ == "__main__":
    grayscale_functional("fruits.jpg", "gray_fruits.jpg")
