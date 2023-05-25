<h2 align="center">
  Reasoning in Large Language Models Through Symbolic Math Word Problems
</h2>
Large language models (LLMs) have revolutionized NLP by solving downstream tasks
with little to no labeled data. Despite their
versatile abilities, the larger question of their
ability to reason remains ill-understood. We effectively describe such by using the
SVAMP-Sym dataset for evaluating symbolic reasoning.

<br>
Below is a sample row detailing a problem from the SVAMP_Sym dataset:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt">ID</th>
    <th class="tg-7btt">Body</th>
    <th class="tg-7btt">Question</th>
    <th class="tg-7btt">Answer</th>
    <th class="tg-7btt">Variables</th>
    <th class="tg-7btt">Numbers</th>
    <th class="tg-fymr">Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">chal-113</td>
    <td class="tg-c3ow">Mary is baking a cake. The recipe calls for &lt;1&gt; cups of sugar and &lt;2&gt; cups of flour. She already put in &lt;3&gt; cups of sugar.</td>
    <td class="tg-c3ow">How many more cups of flour than cups of sugar does she need to add now?</td>
    <td class="tg-c3ow">( &lt;2&gt; - ( &lt;1&gt; - &lt;3&gt; ) )</td>
    <td class="tg-c3ow">['&lt;1&gt;', '&lt;2&gt;', '&lt;3&gt;']</td>
    <td class="tg-c3ow">['14.0', '12.0', '10.0']</td>
    <td class="tg-0pky">Subtraction</td>
  </tr>
</tbody>
</table>
<p style="text-align: justify;">

<br>

#### Dataset specifications

- compatible with python 3.10
- dependencies can be installed using `SVAMP/code/requirements.txt`
// to be added

- `SVAMP ` & ` SVAMP_Sym ` & ` SVAMP_(wxyz, pqrs, ijkl)`:
  - `Data Size:` 1000
  - Complete challenge set to be used for evaluation.

A description of the individual data files in the `Symbolic-MWP-Reasoning/Datasets` directory is given below:

- `Symbolic-MWP-Reasoning/Datasets/SVAMP.csv`
  - Original [SVAMP](https://github.com/arkilpatel/SVAMP) dataset, 1000 MWPs. 

- `Symbolic-MWP-Reasoning/Datasets/SVAMP_Sym.csv`
  - A modified SVAMP dataset where all numerical values are replaced by a tag `<n>`. 

- `Symbolic-MWP-Reasoning/Datasets/Variables/SVAMP_wxyz.csv`
  - A modified SVAMP dataset where all numerical values are replaced by the variables `w, x, y, z`. 

- `Symbolic-MWP-Reasoning/Datasets/Variables/SVAMP_pqrs.csv`
  - A modified SVAMP dataset where all numerical values are replaced by the variables `p, q, r, s`. 

- `Symbolic-MWP-Reasoning/Datasets/Variables/SVAMP_ijkl.csv`
  - A modified SVAMP dataset where all numerical values are replaced by the variables `i, j, k, l`. 


#### Usage

The set of command line arguments available can be seen in the respective `args.py` file. Here, we illustrate running the experiment for cross validation of the ASDiv-A dataset using the Seq2Seq model. Follow the same methodology for running any experiment over any model.

#### Citation

If you use our data or code, please cite our work:

```
Citation
```

For any clarification, comments, or suggestions please contact [Vedant](http://vedantgaur.com/) or [Nikunj](https://github.com/nsaunshi).