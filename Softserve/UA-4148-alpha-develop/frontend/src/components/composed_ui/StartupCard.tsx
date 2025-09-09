import SubscribeStartupButton from "./SubscribeStartupButton";

interface StartupCardProps {
  startup: IStartup;
}

export interface IStartup {
  id: number;
  subject: string;
  idea: string;
  description: string;
  website: string;
  investment_needed: boolean;
  views_count: number;
  created_at: string;
  updated_at: string;
  startup_name: string;
  investor_name: null | string;
}

export function StartupCard({ startup }: StartupCardProps) {
  return (
    <div className="p-4 rounded-md bg-main-bg select-none flex flex-col gap-1">
      <div className="flex items-start justify-between gap-2">
        <p>{startup.startup_name}</p>
        <SubscribeStartupButton id={startup.id} />
      </div>
      <div className="flex flex-col gap-2 h-full">
        <h4 className="text-secondary-black font-bold text-xl font-display">
          {startup.subject}
        </h4>
        <p className="font-display text-secondary-black text-[14px]">
          {startup.description}
        </p>
        <div className="mt-auto flex flex-col gap-2">
          <hr />
          <p className="font-display text-secondary-black text-[12px]">
            Кiлькiсть Переглядiв: {startup.views_count}
          </p>
        </div>
      </div>
    </div>
  );
}
