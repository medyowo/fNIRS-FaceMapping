% displayData function is used to display channel values got from fNIRS.
% data : experiments data from fNIRS measures
% startValue : first channel to display
% endValue : last channel to display
% toDisplay : What value to display between [oxyHb, deoxyHb, totHb]
% displayData 関数は、fNIRSから取得したチャネル値を表示するために使用されます。
% data : fNIRS測定からの実験データ
% startValue : 表示を開始する最初のチャネル
% endValue : 表示を終了する最後のチャネル
% toDisplay : [oxyHb, deoxyHb, totHb] のいずれか、表示する値

function displayData(data, startData, EndData, startChannel, endChannel, toDisplay, graphTitle)
    % For each data
    % 各データについて
    for j=0+startData : EndData
        % Create figure for subplot channels
        % サブプロットチャネル用の図を作成する
        figure('Name',[graphTitle,' | ', 'DATA N°', num2str(j),' - Visualisation of channels ', num2str(startChannel), ' - ', num2str(endChannel)], 'Numbertitle','off');
        
        % For each channel display values
        % 各チャネルの値を表示する
        for k=0+startChannel : endChannel
            % Display data in 2 columns
            % データを2列で表示する
            subplot(round((endChannel-startChannel)/2, TieBreaker="plusinf"),2,k-(startChannel-1));
        
            xlabel('time (seconds)');
            ylabel('Hb');
            title(['channel n°', num2str(k)])
            hold on
            
            % Check each data which is needed to be displayed
            % 表示が必要な各データを確認する
            % Display oxygenated blood graph
            % 酸素化血液のグラフを表示する
            if ismember("oxyHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,6+3*(k-1)}, "Color", "#A2142F");
            end
            
            % Display desoxygenated blood graph
            % 脱酸素血液のグラフを表示する
            if ismember("deoxyHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,7+3*(k-1)}, "Color", "#0072BD")
            end
            
            % Display total blood graph
            % 総血液のグラフを表示する
            if ismember("totalHb", toDisplay)
                plot(data{j}{:,2}, data{j}{:,8+3*(k-1)}, "Color", "#77AC30")
            end
            ylim([-1 1]);
            
            % Display Fourier Transform graph
            % フーリエ変換のグラフを表示する
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
