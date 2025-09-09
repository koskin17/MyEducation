import { Button } from "@/components/ui/button";
import { cn } from "@/libs/utils";
import { useState } from "react";
import { Enterprises } from "../components/composed_ui/Enterprises";
import { Companies } from "../components/composed_ui/Companies";
import { Startups } from "./Startups";

const NAVIGATION_TAB_STYLE = cn(
  "text-secondary-black font-normal text-[16px] md:text-xl font-display underline-offset-6 hover:no-underline"
);

export function EnterprisesAndIndustries() {
  const [tab, setActiveTab] = useState<"all" | "companies" | "startups">("startups");

  return (
    <div className="flex flex-col h-full">
      <div className="w-full max-w-[1304px] px-4 mx-auto">
        <div className="pt-9 md:pt-12 xl:pt-20 flex flex-col md:gap-6 gap-8">
          <h2 className="text-secondary-black font-bold text-2xl md:text-[40px] font-display">
            Підприємства та сектори
          </h2>
          <div className="flex items-center gap-6">
            <TabButton
              title="Усі підприємства"
              isActive={tab === "all"}
              onClick={() => setActiveTab("all")}
            />
            <TabButton
              title="Компанії"
              isActive={tab === "companies"}
              onClick={() => setActiveTab("companies")}
            />
            <TabButton
              title="Стартапи"
              isActive={tab === "startups"}
              onClick={() => setActiveTab("startups")}
            />
          </div>
        </div>
      </div>
      <div className="w-full bg-white pt-8 h-full">
        <div className="w-full max-w-[1304px] px-4 mx-auto">
          {tab === "all" && <Enterprises />}
          {tab === "companies" && <Companies />}
          {tab === "startups" && <Startups />}
        </div>
      </div>
    </div>
  );
}

interface TabButtonProps {
  onClick: () => void;
  isActive: boolean;
  title: string;
}

function TabButton({ onClick, isActive, title }: TabButtonProps) {
  return (
    <Button
      variant={"tertiary"}
      onClick={onClick}
      className={NAVIGATION_TAB_STYLE}
    >
      <div className="flex flex-col gap-2.5">
        {title}
        <div className="relative h-[2px] w-full">
          {isActive && (
            <div className=" w-full h-full bg-black absolute bottom-0" />
          )}
        </div>
      </div>
    </Button>
  );
}
