import openai

openai.api_key = "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"

prompt = input("Enter the theme of texts: ")
texts_amount = int(input("Amount of texts to generate: "))

while True:
    try:
        text_size = int(input("Text size in tokens(maximum size is " + str(4070-prompt.count(' ')) + " tokens): "))
    except ValueError:
        print("The value has to be an integer. Try again.")
    else:
        break

for i in range(texts_amount):
    output = openai.completions.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=text_size
    )
    print(output.choices[0].text)
    with open("Generated Texts/"+prompt + "_" + str(i)+".txt", "w") as f:
        f.write(output.choices[0].text)
        f.close()


