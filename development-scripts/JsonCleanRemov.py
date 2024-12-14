import json

json_data = '''
{
    "id":"2412.04472",
    "submitter":"Luca Bartolomei",
    "authors":"Luca Bartolomei, Fabio Tosi, Matteo Poggi, Stefano Mattoccia",
    "title":"Stereo Anywhere: Robust Zero-Shot Deep Stereo Matching Even Where Either\\n  Stereo or Mono Fail",
    "comments":"Code: https://github.com/bartn8/stereoanywhere - Project page:\\n  https://stereoanywhere.github.io/",
    "journal-ref":null,
    "doi":null,
    "report-no":null,
    "categories":"cs.CV",
    "license":"http://arxiv.org/licenses/nonexclusive-distrib/1.0/",
    "abstract":"  We introduce Stereo Anywhere, a novel stereo-matching framework that combines\\ngeometric constraints with robust priors from monocular depth Vision Foundation\\nModels (VFMs). By elegantly coupling these complementary worlds through a\\ndual-branch architecture, we seamlessly integrate stereo matching with learned\\ncontextual cues. Following this design, our framework introduces novel cost\\nvolume fusion mechanisms that effectively handle critical challenges such as\\ntextureless regions, occlusions, and non-Lambertian surfaces. Through our novel\\noptical illusion dataset, MonoTrap, and extensive evaluation across multiple\\nbenchmarks, we demonstrate that our synthetic-only trained model achieves\\nstate-of-the-art results in zero-shot generalization, significantly\\noutperforming existing solutions while showing remarkable robustness to\\nchallenging cases such as mirrors and transparencies.\\n",
    "versions":[{"version":"v1","created":"Thu, 5 Dec 2024 18:59:58 GMT"}],
    "update_date":"2024-12-06",
    "authors_parsed":[["Bartolomei","Luca",""],["Tosi","Fabio",""],["Poggi","Matteo",""],["Mattoccia","Stefano",""]]
}
'''

# Load JSON data
data = json.loads(json_data)

# Clean the data by replacing unwanted characters
cleaned_data = json.dumps(data).replace("\\n", " ").replace("\\\\", "\\")

# Load the cleaned JSON data back into a dictionary
cleaned_data_dict = json.loads(cleaned_data)


# Fields to remove
fields_to_remove = ["submitter","comments", "journal-ref","doi","report-no","license","versions"]

# Remove unwanted fields
for field in fields_to_remove:
    if field in cleaned_data_dict:
        del cleaned_data_dict[field]

# Print the cleaned JSON data
print(json.dumps(cleaned_data_dict, indent=4))
