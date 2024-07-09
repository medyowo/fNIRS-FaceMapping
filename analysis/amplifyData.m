function additionalData = amplifyData(originalData, methods, nFactorData)
    additionalData = {[1,length(nFactorData * length(originalData))]};
    
    for k=1 : (nFactorData-1)
        method = randsample(methods,1);
        disp("[ADD] Amplify data using " + method + " (" + k + ")")
        
        for i = 1 : length(originalData)
            % Create the new table for Jittered data
            additionalData{i + ((k-1) * 140)} = table('Size', [height(originalData{i}) width(originalData{i})], 'VariableTypes', varfun(@class,originalData{i},'OutputFormat','cell'), 'VariableNames',originalData{i}.Properties.VariableNames);

            % Add multiple properties to precise data 
            additionalData{i + ((k-1)* 140)} = addprop(additionalData{i + ((k-1)* 140)},{'SubjectName', 'ExperimentType', 'ExperimentNumber', 'TestNumber', 'FileName', 'SourceFolder'}, {'table', 'table', 'table', 'table', 'table', 'table'});
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.SubjectName = originalData{i}.Properties.CustomProperties.SubjectName;
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.ExperimentType = originalData{i}.Properties.CustomProperties.ExperimentType;
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.ExperimentNumber = originalData{i}.Properties.CustomProperties.ExperimentNumber;
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.TestNumber = str2double(originalData{i}.Properties.CustomProperties.TestNumber) + (k * 5);
        
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.FileName = strrep(originalData{i}.Properties.CustomProperties.FileName, "_" + originalData{i}.Properties.CustomProperties.TestNumber, "_" + (str2double(originalData{i}.Properties.CustomProperties.TestNumber) + k*5));
            additionalData{i + ((k-1)* 140)}.Properties.CustomProperties.SourceFolder = originalData{i}.Properties.CustomProperties.SourceFolder;

            if ismember("jittering", method)
                additionalData{i + ((k-1)* 140)} = addjitteredData(originalData{i}, additionalData{i + ((k-1)* 140)}, 0.01);
            end

            if ismember("scaling", method)
                additionalData{i + ((k-1)* 140)} = addscaledData(originalData{i}, additionalData{i + ((k-1)* 140)}, [0.90, 1.10]);
            end

            if ismember("warping", method)
                additionalData{i + ((k-1)* 140)} = addwarpedData(originalData{i}, additionalData{i + ((k-1)* 140)}, 0.10, originalData{i}{:, 2});
            end

            additionalData{i + ((k-1)* 140)}{:, 1} = originalData{i}{:, 1};
            additionalData{i + ((k-1)* 140)}{:, 2} = originalData{i}{:, 2};
        end
    end

    additionalData = [originalData, additionalData];
end

function jitteredData = addjitteredData(currentData, currentAdditionalData, jitter_amount)
    noise = jitter_amount * randn(size(currentData{:,6}));
    
    for j = 1 : 22
        currentAdditionalData{:,6+3*(j-1)} = currentData{:,6+3*(j-1)} + noise;
        currentAdditionalData{:,7+3*(j-1)} = currentData{:,7+3*(j-1)} + noise;
        currentAdditionalData{:,8+3*(j-1)} = currentData{:,8+3*(j-1)} + noise;
    end

    jitteredData = currentAdditionalData;
end

function scaledData = addscaledData(currentData, currentAdditionalData, scaling_factor_range)
    scaling_factor = (scaling_factor_range(2) - scaling_factor_range(1)) * rand + scaling_factor_range(1);

    for j = 1 : 22
        currentAdditionalData{:,6+3*(j-1)} = currentData{:,6+3*(j-1)} * scaling_factor;
        currentAdditionalData{:,7+3*(j-1)} = currentData{:,7+3*(j-1)} * scaling_factor;
        currentAdditionalData{:,8+3*(j-1)} = currentData{:,8+3*(j-1)} * scaling_factor;
    end

    scaledData = currentAdditionalData;
end

function warpedData = addwarpedData(currentData, currentAdditionalData, warping_amount, time)
    warp_function = @(x) x + warping_amount * sin(2 * pi * x / max(x));
    random_warp = warp_function(time + warping_amount * randn(size(time)));

    for j = 1 : 22
        currentAdditionalData{:,6+3*(j-1)} = interp1(time, currentData{:,6+3*(j-1)}, random_warp, 'linear', 'extrap');
        currentAdditionalData{:,7+3*(j-1)} = interp1(time, currentData{:,7+3*(j-1)}, random_warp, 'linear', 'extrap');
        currentAdditionalData{:,8+3*(j-1)} = interp1(time, currentData{:,8+3*(j-1)}, random_warp, 'linear', 'extrap');
    end

    warpedData = currentAdditionalData;
end
