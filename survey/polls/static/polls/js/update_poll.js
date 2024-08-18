document.addEventListener("DOMContentLoaded", function () {
  const addChoiceButton = document.querySelector(".add-row");
  const totalFormsInput = document.getElementById("id_choice_set-TOTAL_FORMS");

  if (addChoiceButton) {
    addChoiceButton.addEventListener("click", function (e) {
      e.preventDefault();
      const formCount = parseInt(totalFormsInput.value);
      const newForm = document.querySelector(".choice-form").cloneNode(true);
      const formRegex = RegExp(`choice_set-(\\d+)-`, "g");

      newForm.innerHTML = newForm.innerHTML.replace(
        formRegex,
        `choice_set-${formCount}-`
      );
      document
        .querySelector(".choice-form")
        .parentNode.insertBefore(newForm, addChoiceButton);

      totalFormsInput.value = formCount + 1;
    });
  }
});
