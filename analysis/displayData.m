% displayData function is used to display channel values got from fNIRS.
% data : experiments data from fNIRS measures
% startValue : first channel to display
% endValue : last channel to display
% toDisplay : What value to display between [oxyHb, deoxyHb, totHb]
function displayData(data, startValue, endValue, toDisplay)

% Create figure for subplot channels
figure('Name',['Visualisation of channels ', num2str(startValue), ' - ', num2str(endValue)], 'Numbertitle','off');

% For each channel display values
for k=0+startValue : endValue
    % Display data in 2 columns
    subplot(round((endValue-startValue)/2, TieBreaker="plusinf"),2,k-(startValue-1));

    xlabel('time (seconds)');
    ylabel('Hb');
    title(['channel n°', num2str(k)])
    hold on
    
    % Check each data which is needed to be displayed
    if ismember("oxyHb", toDisplay)
        plot(data{1}{:,2}, data{1}{:,6+3*(k-1)}, "Color", "#A2142F");
    end

    if ismember("deoxyHb", toDisplay)
        plot(data{1}{:,2}, data{1}{:,7+3*(k-1)}, "Color", "#0072BD")
    end

    if ismember("totalHb", toDisplay)
        plot(data{1}{:,2}, data{1}{:,8+3*(k-1)}, "Color", "#77AC30")
    end

    legend(toDisplay)
    ylim([-1 1])
    hold off
end

