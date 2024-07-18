function dataHaveBeenSaved = saveData(data, folderName)
    % Check if Filtered Data Folder has been created, if not do it
    if ~exist(folderName, 'dir')
       mkdir(folderName)
    end

    for i = 1 : length(data)
        subjectFolder = folderName + data{i}.Properties.CustomProperties.SubjectName + "\";
        fileFolder = subjectFolder + data{i}.Properties.CustomProperties.ExperimentType + data{i}.Properties.CustomProperties.ExperimentNumber + "\";

        % Check if Subject Folder has been created, if not do it
        if ~exist(subjectFolder, 'dir')
            disp("[Create] " + subjectFolder)
            mkdir(subjectFolder)
        end
        % Check if experiment{X}/temoin{X} Folder has been created, if not do it
        if ~exist(fileFolder, 'dir')
            disp("[Create] " + fileFolder)
            mkdir(fileFolder)
        end
        
        disp("[Save] " + strrep(data{i}.Properties.CustomProperties.FileName, '.csv', '-filtered.csv'))
        writetable(data{i}, fileFolder + strrep(data{i}.Properties.CustomProperties.FileName, '.csv', '-filtered.csv'))
    end

    dataHaveBeenSaved = true;
end

