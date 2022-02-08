import torch

import wandb
from info_extraction.model import Scorer
from info_extraction.data import Dataset
from info_extraction.utils import make_data
from info_extraction.args import parser

def train(args):
    wandb.init(
        settings=wandb.Settings(start_method="fork"),
        project='info_extraction',
        entity=args.entity,
        config=vars(args),
    )
    wandb.run.name = (
        f"near:{args.near_size}-far:{args.far_size}-per_page:{args.it_per_page}"
        + f"dim:{args.emb_dim}-batch_size:{args.batch_size}-epochs:{args.num_epochs}"
        + f"-lr:{args.lr}"
    )

    field, candidate_pos, neighbor_text, neighbor_pos, label, field_dict, vocab_dict = make_data(
        near_size=args.near_size,
        far_size=args.far_size,
        it_per_page=args.it_per_page
    )

    dataset = Dataset(field, candidate_pos, neighbor_text, neighbor_pos, label)

    model = Scorer(emb_dim=args.emb_dim, vocab_size=len(vocab_dict), n_fields=len(field_dict))

    loader = torch.utils.data.DataLoader(dataset, batch_size=args.batch_size)

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    loss_fn = torch.nn.BCELoss()
    counter = 0
    for _ in range(args.num_epochs):
        for sample in loader:
            f, cp, nt, npos, y = sample
            pred = model(f, cp, nt, npos)
            optimizer.zero_grad()
            loss = loss_fn(pred, y.squeeze(1))
            loss.backward()
            optimizer.step()
            counter += 1
            if counter % 10:
                wandb.log({"Loss": loss.item()}, step=counter)

    torch.save(model.state_dict(), 'model.pt')
    wandb.save('model.pt')

if __name__ == "__main__":
    args = parser.parse_args()
    train(args)