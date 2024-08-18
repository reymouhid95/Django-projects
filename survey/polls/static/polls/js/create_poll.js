document.addEventListener("DOMContentLoaded", function () {
  const addChoiceButton = document.getElementById("add-choice");
  const choicesContainer = document.getElementById("choices");
  const choiceCountInput = document.getElementById("choice-count");

  let choiceCount = parseInt(choiceCountInput.value);

  addChoiceButton.addEventListener("click", function () {
    const newChoiceDiv = document.createElement("div");
    newChoiceDiv.className = "choice-form";

    const newChoiceLabel = document.createElement("label");
    newChoiceLabel.htmlFor = `id_${choiceCount}-choice_text`;
    newChoiceLabel.textContent = `Choice ${choiceCount + 1}:`;

    const newChoiceInput = document.createElement("input");
    newChoiceInput.type = "text";
    newChoiceInput.name = `${choiceCount}-choice_text`;
    newChoiceInput.id = `id_${choiceCount}-choice_text`;
    newChoiceInput.maxLength = "200";
    newChoiceInput.required = true;

    newChoiceDiv.appendChild(newChoiceLabel);
    newChoiceDiv.appendChild(newChoiceInput);

    choicesContainer.appendChild(newChoiceDiv);

    choiceCount++;
    choiceCountInput.value = choiceCount;
  });
});
