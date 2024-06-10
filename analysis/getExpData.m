function expArrays = getExpData()
    addpath("../fNIRS-FaceMapping/")
    
    myFolder = 'measurements/cleaned';
    filePattern = fullfile(myFolder, '**/*.csv');
    expArrays = filesToArray(dir(filePattern));
end

function extractedArrays = filesToArray(filesList)
    extractedArrays = {[1,length(filesList)]};
    for k = 1 : length(filesList)
        fLink = append(filesList(k).folder, "\", filesList(k).name);
        extractedArrays{k} = extractExpDataFromFile(fLink);
    end
end

function extractedData = extractExpDataFromFile(fileName)
    opts=detectImportOptions(fileName, 'NumHeaderLines',2);
    opts.VariableNamesLine = 1;
    opts.VariableUnitsLine = 2;
    opts.Delimiter =',';

    extractedData = readtable(fileName, opts, 'ReadVariableNames', true);
end