# Assignment Graphs

#### Martin Silva (#030854159), Zachary Padilla (#033497475)

## Usage Instructions
- ``--plot`` outputs are stored in ``.png`` files.
- When invoking ``--multi_BFS``, ``--plot`` must be included within the same command if you wish to plot the BFS trees. This is as users may want to view the default graph instead.
- Invoking ``--multi_BFS`` on a previously-existing graph will modify the corresponding ``.gml`` file to include all shortest paths.
-   This behavior is also true of directly invoking ``--multi_BFS`` and ``--output`` together.
- ``out_graph_file.gml`` is the default name for outputted graphs if one is not specified.

## Description of Implementation
- All instructions were followed as listed—interpretations were made where needed.
- Images were originally represented in Pyplot windows, though this seemed system-dependent as it didn't work within certain IDEs. As such, they are saved as ``.png`` files.

## Examples of Commands and Outputs

``> python ./graph.py --create_random_graph 200 1.5 --analyze``
```
Connected Components:
[['0', '155', '147', '199', '152', '191', '156', '183', '169', '192', '187', '190', '158', '135', '153', '163', '189', '184', '151', '182', '168', '149', '134', '1
79', '197', '22', '194', '138', '193', '159', '136', '195', '109', '175', '167', '172', '144', '161', '164', '142', '198', '196', '104', '111', '132', '88', '31', 
'188', '141', '126', '64', '162', '59', '185', '180', '170', '140', '146', '166', '176', '173', '99', '178', '123', '186', '181', '148', '120', '115', '133', '105'
, '117', '89', '112', '137', '139', '76', '116', '121', '113', '107', '15', '122', '84', '45', '177', '67', '131', '101', '171', '130', '127', '129', '128', '154',
 '145', '160', '56', '110', '119', '108', '100', '165', '157', '174', '150', '28', '90', '114', '51', '92', '93', '82', '71', '54', '23', '75', '118', '57', '74', 
'87', '35', '97', '79', '86', '63', '80', '91', '102', '83', '27', '10', '65', '98', '96', '124', '94', '52', '77', '95', '55', '48', '46', '19', '58', '47', '106'
, '68', '11', '30', '72', '5', '125', '9', '49', '42', '26', '2', '43', '81', '40', '41', '33', '6', '66', '18', '20', '50', '1', '62', '7', '44', '37', '53', '8', '24', '16', '39', '61', '60', '4', '70', '78', '103', '32', '25', '85', '143', '69', '12', '21', '29', '34', '36', '38', '3', '14', '73', '13', '17']]
Cycle Detection:
['156', '183', '169', '192', '187', '190', '158', '135']
Isolated Nodes: []
Graph Density: 0.036331658291457285
Average Shortest Path Length: 2.8804020100502514
```
``> python graph.py --input example_graph.gml --plot``

(Saved as ``graph_plot930289.png``)\
<img width="640" height="480" alt="graph_plot930289" src="https://github.com/user-attachments/assets/761ace42-6cec-4274-b410-c09d94db37bb" />

``> python ./graph.py --create_random_graph 200 1.5 --multi_BFS 0 5 20 --plot``
<br></br>
(Saved as ``bft_plot0.png``)\
<img width="640" height="480" alt="bft_plot0" src="https://github.com/user-attachments/assets/50b5e504-3039-492b-86da-ab73e97085af" />\
(Saved as ``bft_plot1.png``)\
<img width="640" height="480" alt="bft_plot1" src="https://github.com/user-attachments/assets/1669c9c6-3a89-422f-a4ec-54a16ccec7b1" />\
(Saved as ``bft_plot2.png``)\
<img width="640" height="480" alt="bft_plot2" src="https://github.com/user-attachments/assets/885ad9a5-ba46-455f-a878-e090b1a296f7" />
