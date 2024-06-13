function expArrays = getExpData()
    addpath("../fNIRS-FaceMapping/")
    warning('OFF', 'MATLAB:table:ModifiedAndSavedVarnames')
    
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
    disp("[Extracting] " + fileName)
    opts=detectImportOptions(fileName, 'NumHeaderLines',2);
    opts.VariableNamesLine = 1;
    opts.VariableUnitsLine = 2;
    opts.Delimiter =',';

    extractedData = readtable(fileName, opts, 'ReadVariableNames', true);
    extractedData = renamevars(extractedData,["Var1","Var2","Var3","x_1","x_2"],["index","time","task","mark","count"]);
    
    toDelete = extractedData.time > 60;
    extractedData(toDelete,:) = [];
    disp("[Job complete]")
end