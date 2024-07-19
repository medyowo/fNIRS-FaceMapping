% getExpData is use to get experimental data from specified folder
% The structure of get data is as following :
% cell [140] expArrays -> table ['index', 'time', 'task', 'mark', 'count', 'channels[1-22]_[∅-2]']
% getExpData は、指定されたフォルダーから実験データを取得するために使用されます
% データの構造は以下の通りです：
% セル [140] expArrays -> テーブル ['index', 'time', 'task', 'mark', 'count', 'channels[1-22]_[∅-2]']

function expArrays = getExpData(myFolder)
    % Change path to repo folder path
    % リポジトリフォルダーのパスに変更する
    addpath("../fNIRS-FaceMapping/")

    % Disable warning from readtable() function
    % readtable() 関数からの警告を無効にする
    warning('OFF', 'MATLAB:table:ModifiedAndSavedVarnames')
    
    % Get every file in myFolder folder and call filesToArray() function
    % myFolder フォルダー内のすべてのファイルを取得し、filesToArray() 関数を呼び出す
    filePattern = fullfile(myFolder, '**/*.csv');
    expArrays = filesToArray(dir(filePattern));
end

% This function loop on every single files in data folder
% この関数は、データフォルダー内のすべてのファイルをループ処理します
function extractedArrays = filesToArray(filesList)
    % Create extracted data table
    % 抽出されたデータテーブルを作成する
    extractedArrays = {[1,length(filesList)]};
    for k = 1 : length(filesList)
        % Get file link and call function to extract file content
        % ファイルリンクを取得し、ファイル内容を抽出するための関数を呼び出す
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
    % 抽出パラメータを変更する：
    % - 行1から3を抽出しない
    % - 変数名は行1に
    % - 変数単位は行2に
    % - 区切り文字は ,
    opts=detectImportOptions(fileName, 'NumHeaderLines',3);
    opts.VariableNamesLine = 1;
    opts.VariableUnitsLine = 2;
    opts.Delimiter =',';
    
    % Read table content and change bad naming for some variable names as
    % well as removing first useless line
    % テーブルの内容を読み込み、一部の変数名の不適切な名前を変更し、
    % 最初の不要な行を削除する
    extractedData = readtable(fileName, opts, 'ReadVariableNames', true);
    extractedData = renamevars(extractedData,["Var1","Var2","Var3","x_1","x_2"],["index","time","task","mark","count"]);
    extractedData{:, "index"} = extractedData{:, "index"} - 1;
    
    % Normalize data duration (every data > 60s are deleted)
    % データの期間を正規化する（60秒を超えるデータは削除されます
    toDelete = extractedData.time > 50;
    extractedData(toDelete,:) = [];
    
    % Extract info from file link
    % ファイルリンクから情報を抽出する
    fileArgs = split(fileName, "\cleaned\");
    fileInfo = split(fileArgs(2), "\");
    
    % Add multiple properties to precise data
    % データを精密化するために複数のプロパティを追加する
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