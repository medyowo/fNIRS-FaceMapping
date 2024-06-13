expArrays = getExpData();

noise_yo = expArrays{:, 5};

displayData(expArrays, 1, 2, 1, 6, ["oxyHb", "deoxyHb"])
displayData(expArrays, 1, 1, 7, 12, ["oxyHb", "deoxyHb"])
displayData(expArrays, 1, 1, 13, 18, ["oxyHb", "deoxyHb"])
displayData(expArrays, 1, 1, 19, 22, ["oxyHb", "deoxyHb", "totalHb"])