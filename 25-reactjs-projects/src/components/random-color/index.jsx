/*import { useEffect, useState } from "react";

export default function RandomColor() {
  const [typeOfColor, setTypeOfColor] = useState("hex");
  const [color, setColor] = useState("#000000");

  function randomColorUtility(length) {
    return Math.floor(Math.random() * length);
  }

  function handleCreateRandomHexColor() {
    // #678765
    const hex = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
    let hexColor = "#";

    for (let i = 0; i < 6; i++) {
      hexColor += hex[randomColorUtility(hex.length)];
    }
    setColor(hexColor);
  }

  function handleCreateRandomRgbColor() {
    const r = randomColorUtility(256);
    const g = randomColorUtility(256);
    const b = randomColorUtility(256);

    setColor(`rgb(${r},${g}, ${b})`);
  }

  useEffect(() => {
    if (typeOfColor === "rgb") handleCreateRandomRgbColor();
    else handleCreateRandomHexColor();
  }, [typeOfColor]);

  return (
    <div
      style={{
        width: "100vw",
        height: "100vh",
        background: color,
      }}
    >
      <button onClick={() => setTypeOfColor("hex")}>Create HEX Color</button>
      <button onClick={() => setTypeOfColor("rgb")}>Create RGB Color</button>
      <button
        onClick={
          typeOfColor === "hex"
            ? handleCreateRandomHexColor
            : handleCreateRandomRgbColor
        }
      >
        Generate Random Color
      </button>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          color: "#fff",
          fontSize: "60px",
          marginTop: "50px",
          flexDirection  :'column',
          gap :'20px'
        }}
      >
        <h3>{typeOfColor === "rgb" ? "RGB Color" : "HEX Color"}</h3>
        <h1>{color}</h1>
      </div>
    </div>
  );
} */

import { useEffect, useState } from "react";

// Utility function to generate a random number up to a given limit
function getRandomNumber(limit) {
  return Math.floor(Math.random() * limit);
}

// Generate a random HEX color
function generateRandomHexColor() {
  const hexChars = "0123456789ABCDEF";
  let hexColor = "#";

  for (let i = 0; i < 6; i++) {
    hexColor += hexChars[getRandomNumber(16)];
  }

  return hexColor;
}

// Generate a random RGB color
function generateRandomRgbColor() {
  const r = getRandomNumber(256);
  const g = getRandomNumber(256);
  const b = getRandomNumber(256);

  return `rgb(${r},${g},${b})`;
}

export default function RandomColor() {
  const [typeOfColor, setTypeOfColor] = useState("hex");
  const [color, setColor] = useState("#000000");

  // Function to generate color based on the type
  function generateColor() {
    const newColor =
      typeOfColor === "hex" ? generateRandomHexColor() : generateRandomRgbColor();
    setColor(newColor);
  }

  useEffect(() => {
    generateColor();
  }, [typeOfColor]);

  // Styles
  const containerStyles = {
    width: "100vw",
    height: "100vh",
    background: color,
  };

  const buttonStyles = {
    padding: "10px 20px",
    fontSize: "16px",
    margin: "5px",
    cursor: "pointer",
  };

  const colorDisplayStyles = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    color: "#fff",
    fontSize: "60px",
    marginTop: "50px",
    flexDirection: "column",
    gap: "20px",
  };

  return (
    <div style={containerStyles}>
      <button style={buttonStyles} onClick={() => setTypeOfColor("hex")}>
        Create HEX Color
      </button>
      <button style={buttonStyles} onClick={() => setTypeOfColor("rgb")}>
        Create RGB Color
      </button>
      <button style={buttonStyles} onClick={generateColor}>
        Generate Random Color
      </button>
      <div style={colorDisplayStyles}>
        <h3>{typeOfColor === "rgb" ? "RGB Color" : "HEX Color"}</h3>
        <h1>{color}</h1>
      </div>
    </div>
  );
}