% displayData function is used to display channel values got from fNIRS.
% data : experiments data from fNIRS measures
% startValue : first channel to display
% endValue : last channel to display
% toDisplay : What value to display between [oxyHb, deoxyHb, totHb]
function displayData(data, startData, EndData, startChannel, endChannel, toDisplay, graphTitle)
    %for each data
    for j=0+startData : EndData
        % Create figure for subplot channels
        figure('Name',[graphTitle,' | ', 'DATA N°', num2str(j),' - Visualisation of channels ', num2str(startChannel), ' - ', num2str(endChannel)], 'Numbertitle','off');
        
        % For each channel display values
        for k=0+startChannel : endChannel
            % Display data in 2 columns
            subplot(round((endChannel-startChannel)/2, TieBreaker="plusinf"),2,k-(startChannel-1));
        
            xlabel('time (seconds)');
            ylabel('Hb');
            title(['channel n°', num2str(k)])
            hold on
            
            % Check each data which is needed to be displayed
            if ismember("oxyHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,6+3*(k-1)}, "Color", "#A2142F");
            end
        
            if ismember("deoxyHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,7+3*(k-1)}, "Color", "#0072BD")
            end
        
            if ismember("totalHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,8+3*(k-1)}, "Color", "#77AC30")
            end
            ylim([-1 1]);

            if ismember("ft", toDisplay)
                plot(data{j}{:,1}, data{j}{:,k+1}, "Color", "#7E2F8E")
                xlabel('frequency (Hz)');
                ylabel('Hb');
                ylim([min(data{j}{:,k+1}), max(data{j}{:,k+1})]);
            end
        
            legend(toDisplay)
            hold off
        end
    end
