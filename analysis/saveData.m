% SaveData is used to save filtered and amplified data in respective
% folders. 
% SaveData は、フィルタリングされたデータ
% と増幅されたデータをそれぞれのフォルダーに保存するために使用されます。
function dataHaveBeenSaved = saveData(data, folderName)
    % Check if Filtered Data Folder has been created, if not do it
    % フィルターデータフォルダーが作成されているか確認し、
    % 作成されていない場合は作成する
    if ~exist(folderName, 'dir')
       mkdir(folderName)
    end

    for i = 1 : length(data)
        subjectFolder = folderName + data{i}.Properties.CustomProperties.SubjectName + "\";
        fileFolder = subjectFolder + data{i}.Properties.CustomProperties.ExperimentType + data{i}.Properties.CustomProperties.ExperimentNumber + "\";

        % Check if Subject Folder has been created, if not do it
        % サブジェクトフォルダーが作成されているか確認し、
        % 作成されていない場合は作成する
        if ~exist(subjectFolder, 'dir')
            disp("[Create] " + subjectFolder)
            mkdir(subjectFolder)
        end
        % Check if experiment{X}/temoin{X} Folder has been created, if not do it
        % experiment{X}/temoin{X} フォルダーが作成されているか確認し、
        % 作成されていない場合は作成する
        if ~exist(fileFolder, 'dir')
            disp("[Create] " + fileFolder)
            mkdir(fileFolder)
        end
        
        disp("[Save] " + strrep(data{i}.Properties.CustomProperties.FileName, '.csv', '-filtered.csv'))
        writetable(data{i}, fileFolder + strrep(data{i}.Properties.CustomProperties.FileName, '.csv', '-filtered.csv'))
    end

    dataHaveBeenSaved = true;
end

