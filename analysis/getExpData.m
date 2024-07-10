% getExpData is use to get experimental data from specified folder
% The structure of get data is as following :
% cell [140] expArrays -> table ['index', 'time', 'task', 'mark', 'count', 'channels[1-22]_[∅-2]'] 
function expArrays = getExpData(myFolder)
    % Change path to repo folder path
    addpath("../fNIRS-FaceMapping/")

    % Disable warning from readtable() function
    warning('OFF', 'MATLAB:table:ModifiedAndSavedVarnames')
    
    % Get every file in myFolder folder and call filesToArray() function
    filePattern = fullfile(myFolder, '**/*.csv');
    expArrays = filesToArray(dir(filePattern));
end

% This function loop on every single files in data folder
function extractedArrays = filesToArray(filesList)
    % Create extracted data table
    extractedArrays = {[1,length(filesList)]};
    for k = 1 : length(filesList)
        % Get file link and call function to extract file content
        fLink = append(filesList(k).folder, "\", filesList(k).name);
        extractedArrays{k} = extractExpDataFromFile(fLink);
    end
end

function extractedData = extractExpDataFromFile(fileName)
    disp("[Extracting] " + fileName)

    % Change extraction parameters :
    % - Don't extract lines 1 to 3
    % - Variable Names on line 1
    % - Varaible Units on line 2
    % - Delimiter is ,
    opts=detectImportOptions(fileName, 'NumHeaderLines',3);
    opts.VariableNamesLine = 1;
    opts.VariableUnitsLine = 2;
    opts.Delimiter =',';
    
    % Read table content and change bad naming for some variable names as
    % well as removing first useless line
    extractedData = readtable(fileName, opts, 'ReadVariableNames', true);
    extractedData = renamevars(extractedData,["Var1","Var2","Var3","x_1","x_2"],["index","time","task","mark","count"]);
    extractedData{:, "index"} = extractedData{:, "index"} - 1;
    
    % Normalize data duration (every data > 60s are deleted)
    toDelete = extractedData.time > 60;
    extractedData(toDelete,:) = [];
    
    % Extract info from file link   
    fileArgs = split(fileName, "\cleaned\");
    fileInfo = split(fileArgs(2), "\");
    
    % Add multiple properties to precise data 
    extractedData = addprop(extractedData,{'SubjectName', 'ExperimentType', 'ExperimentNumber', 'TestNumber', 'FileName', 'SourceFolder'}, {'table', 'table', 'table', 'table', 'table', 'table'});
    extractedData.Properties.CustomProperties.SubjectName = fileInfo(1);
    extractedData.Properties.CustomProperties.ExperimentType = regexprep(fileInfo(2), '[0-9]', '');
    
    numbers = split(regexprep(fileInfo(end), '[a-zA-Z.]+', ''), "_");
    extractedData.Properties.CustomProperties.ExperimentNumber = regexprep(fileInfo(2), '[a-zA-Z_]+', '');
    extractedData.Properties.CustomProperties.TestNumber = numbers{3};

    extractedData.Properties.CustomProperties.FileName = fileInfo(end);
    extractedData.Properties.CustomProperties.SourceFolder = fileArgs(1);
    
    disp("[Job complete]")
end