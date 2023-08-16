
// Prompt user to select an image
run("Open...");

// Get metadata from image description
metadata = getInfo("image.description");

// Find position of "scale" key
start = indexOf(metadata, "\"scale\": \"");
if (start == -1) {
  print("Scale key not found in metadata");
} else {
  // Extract scale value as substring
  end = indexOf(metadata, "\"", start + 10);
  if (end == -1) {
    print("Scale value not found in metadata");
  } else {
    scale = substring(metadata, start + 10, end);
    //print("Scale: " + scale);

  }
}
// Set the scale of the program to the pixel size
run("Set Scale...", "distance="+scale+" known=1 pixel=1 unit=mm");
