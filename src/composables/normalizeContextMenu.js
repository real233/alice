import perks from "./perks";

export default (mouseX, mouseY) => {
  const scope = perks.getElem("app", "id");
  const contextMenu = perks.getElem("context-menu", "class");
  // ? compute what is the mouse position relative to the container element (scope)
  let { left: scopeOffsetX, top: scopeOffsetY } = scope.getBoundingClientRect();

  scopeOffsetX = scopeOffsetX < 0 ? 0 : scopeOffsetX;
  scopeOffsetY = scopeOffsetY < 0 ? 0 : scopeOffsetY;

  const scopeX = mouseX - scopeOffsetX;
  const scopeY = mouseY - scopeOffsetY;

  // ? check if the element will go out of bounds
  const outOfBoundsOnX = scopeX + contextMenu.clientWidth > scope.clientWidth;

  const outOfBoundsOnY = scopeY + contextMenu.clientHeight > scope.clientHeight;

  let normalizedX = mouseX;
  let normalizedY = mouseY;

//   console.log(mouseX, mouseY);
  // ? normalize on X
  if (outOfBoundsOnX) {
    normalizedX = scopeOffsetX + scope.clientWidth - contextMenu.clientWidth;
  }

  // ? normalize on Y
  if (outOfBoundsOnY) {
    normalizedY = scopeOffsetY + scope.clientHeight - contextMenu.clientHeight;
  }

  console.log(normalizedX, normalizedY);

  return { normalizedX, normalizedY };
};